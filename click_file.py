import click 
import random
import string

def autogen(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



@click.group()
def main():
    """Building a simpldocumentatione aws environment"""
    

@click.command()
@click.option("--name","-n",default=autogen(5),help="Stack name")
@click.option("--compute","-c",default="t2.micro",help="Compute machine type")
@click.option("--region","-r",default="us-west-1",help="Environment region")
@click.option("--generate-template-only","-t")
@click.option("--deploy","-d")
@click.option("--output","-o")
def aws_tool(name,compute,region,generate_template_only,deploy,output):
    

main.add_command(aws_tool)    

if __name__=="__main__":
    main()

    