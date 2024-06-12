import subprocess
import sys, os

args: list[str] = sys.argv

if len(args) < 2:
    exit("Esperava arquivo para validar")
if not args[1].endswith(".py"):
    exit("Esperava arquivo .py")

def validate_answer(result, answer):
    result = result.strip().replace('\r\n', '\n')
    answer = answer.strip().replace('\r\n', '\n')
    return result == answer

def run_program(path, input_file):
    program = subprocess.Popen(["python", path],
                stdin=input_file,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True)
    stdout, stderr = program.communicate()
    if program.returncode != 0:
        print(stderr)
    return [stdout, stderr]

folder_name = "checks\\" + args[1].split(".")[0]

#conut number of tests
tests_needed = len([name for name in os.listdir(os.path.join(os.getcwd(), folder_name))])
for test in range(tests_needed):
    check_path = folder_name + "\\" + str(test+1)
    print(check_path)
    checks_needed = len([name for name in os.listdir(os.path.join(os.getcwd(), check_path))]) // 2

    print(f"Teste {test + 1}:")

    #loop through checks
    for i in range(1, checks_needed + 1):
        input_file = open(f"{check_path}\\{i}.in", "rb")
        answer_file = open(f"{check_path}\\{i}.sol", "r")
        answer_content = answer_file.read()
        stdout, stderr = run_program(args[1], input_file)
        if validate_answer(stdout, answer_content):
            print(f"  Check {i} está correto")
        else:
            print(f"  Check {i} está incorreto")