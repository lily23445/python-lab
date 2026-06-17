import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

client= Groq(api_key=os.getenv('GROQ_API_KEY'))

def ask(question:str,system_prompt,temperature:list[float]=[0.0,0.5],):
    lst=[]
    for i in temperature:
        print(f"\n{'─'*40}")
        print(f"Temperature: {i}")
        print(f"{'─'*40}")
        response=client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role":"system","content":system_prompt},
                {"role":"user","content":question}
            ],
            stream=True,
            temperature=i,
            )

        txt=''
        for chunk in response:
            token=chunk.choices[0].delta.content or ""
            print(token,end='',flush=True)
            txt+=token
        lst.append(txt)

    return lst


if __name__ == "__main__":

    system_prompt="""
    you are an helpful assistant that helps with all fields give factual but also
    creative answers.answers have to direct and short.
    """

    question = input("Ask anything: ")
    r=ask(question,system_prompt)

    print("\n📊 Token Summary:")
    for i, (response, temp) in enumerate(zip(r, [0.0, 0.5])):
        print(f"  Temperature {temp}: ~{len(response) // 4} tokens")
    print(f"  Total: ~{sum(len(x) // 4 for x in r)} tokens")

    