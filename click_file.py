import click 
import random
import string
import os

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
@click.option("--generate-template-only","-t",type=bool)
@click.option("--deploy","-d",type=bool)
@click.option("--output","-o")
def aws_tool(name,compute,region,generate_template_only,deploy,output):
    if(generate_template_only!=None and deploy!=None):
        click.echo("Use either genetare template only or deploy but both cannot be used simultaniously")

    else:
        if(generate_template_only==None and deploy==True): 
            os.system("aws cloudformation create-stack --stack-name {} --template-body file://instance.json --parameters ParameterKey=InstanceType,ParameterValue={} ".format(name,compute))
            if(output!=None):
                os.system("cp instance.json {}".format(output))
        elif(generate_template_only==True and deploy==None): 
            os.system("cat instance.json")
            if(output!=None):
                os.system("mv instance.json {}".format(output))


main.add_command(aws_tool)    

if __name__=="__main__":
    main()

    