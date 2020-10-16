import click 
import random
import string
import os
import boto3

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
@click.argument("template_flie_location",nargs=1)
@click.argument("key_file",nargs=1)
def aws_tool(name,compute,region,generate_template_only,deploy,output,template_flie_location,key_file):
    
    if(generate_template_only!=None and deploy!=None):
        click.echo("Use either genetare template only or deploy but both cannot be used simultaniously")

    else:
        if(deploy==True): 
            client = boto3.client("cloudformation")
            client.create_stack( StackName=name,TemplateURL=template_flie_location,
                    Parameters=[
                                {
                                    'ParameterKey': "KeyName",
                                    'ParameterValue': key_file
                                },
                                {
                                    'ParameterKey': "InstanceType",
                                    'ParameterValue': compute 
                                    },
                                ])
            
            
        else: 
            os.system("cat instance.json")
            
    if(output!=None):
        os.system("cp instance.json {}".format(output))

main.add_command(aws_tool)    

if __name__=="__main__":
    main()

    