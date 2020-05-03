#Student_name: Harwinddranath Muralitheran
#Student_ID: 22254937
#CITS2401 - Lab_2_Part_4


def honeybee(h0,f0,L,w,m,n):
    
    parameters = [h0,f0,L,w,m,n]
    
    for i in range(len(parameters)):
        if parameters[i] < 0:
            print("Please enter positive integers only.")
            return 
    
    h_list = [round(h0)]
    f_list = [round(f0)]
    
    for ii in range(1,n+1):
        N = h_list[-1] + f_list[-1]
        h = round(h_list[-1] + L * (N / (w + N)) - h_list[-1] * (0.25 - 0.75 * (f_list[-1] / (N + 0.001))))
        if h < 0:
            h = 0
        f = round(f_list[-1] + h_list[-1] * (0.25 - 0.75 * (f_list[-1] / (N + 0.001))) - m * f_list[-1])
        if f < 0:
            f_list.append(0)
        else:
            f = round(f,0)
            f_list.append(int(f))
        h_list.append(h)
    H_max = max(h_list)
    F_max = max(f_list)
    
    return (h_list, f_list, H_max, F_max)