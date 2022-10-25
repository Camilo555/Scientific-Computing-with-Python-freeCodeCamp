def arithmetic_arranger(problems, display=False):
    num_1 = []
    num_2= []
    total= []
    sig = []
    num_lens = []
    max_len = []
    long = []

    string_1 = '' 
    string_2 = ''
    lines = ''
    result = ''
    
    #try:
    if len(problems)>5:
        return "Error: Too many problems."

    for pro in problems:
            
        ad = pro.split()
        if not ad[0].isdigit() or not ad[2].isdigit():
            return 'Error: Numbers must only contain digits.'
            break
        a = int(ad[0])
        op = ad[1]
        b = int(ad[2])

        if len(str(a))> 4 or len(str(b))> 4:
            return 'Error: Numbers cannot be more than four digits.'
            break

        num_1.append(str(a))
        num_2.append(str(b))
        sum = a+b
        sub = a-b
        sig.append(op)
        if op == '+':
            total.append(str(sum))
        elif op== '-':
            total.append(str(sub))
        else:
            return "Error: Operator must be '+' or '-'."
            break

    #DISPLAY
    for i in range(len(num_1)):
        len_num = (len(num_1[i]), len(num_2[i]))
        num_lens.append(len_num)
        max_len.append(max(num_lens[i]))

    for i in range(len(num_1)):
        long.append(2+max_len[i])
        j = ''
    
        if i==len(num_1)-1:
            string_1 += num_1[i].rjust(long[i])+"\n"# FIRST LINE
            string_2 += sig[i]+num_2[i].rjust(long[i]-1)+"\n"# SECOND LINE
            lines += j.rjust(long[i],'-')# LINES
            result += total[i].rjust(long[i])

        else:
            string_1 += num_1[i].rjust(long[i])+'    ' # FIRST LINE
            string_2 += sig[i]+num_2[i].rjust(long[i]-1)+'    ' # SECOND LINE
            lines += j.rjust(long[i],'-')+'    ' # LINES
            result += total[i].rjust(long[i])+'    ' # RESULTS

            

    string = string_1 + string_2 +  lines
    string_results = string +"\n"+ result


    if display:
        arranged_problems = string_results #print(string_results, end='')
    else:
        arranged_problems = string #print(string, end='')
    #except AssertionError as msg:
        #arranged_problems = print(msg)
    return arranged_problems