import math as mt

N = 130
num_of_characters = 7
t_variable = 3
t_model = 150
average_list, service_list, rejected_list, bandwidth = [], [], [], []


def randomizing(num_of_characters, t_variable, t_model, n):
    mods_meaning = 2 ** num_of_characters
    lambda_variable = (8 * t_variable) + 3
    list_of_our_variables = [n / mods_meaning]
    for _ in range(t_model):
        our_value = (n * lambda_variable) % mods_meaning
        list_of_our_variables.append(our_value / mods_meaning)
        n = our_value
    return list_of_our_variables


def printing(a, b, lyamda, myu, sigma):
    for i in range(N):
        n = 2 * i + 3
        print(f"Experiment count is {i}")
        our_variable = randomizing(num_of_characters, t_variable, t_model, n)

        def getting_t_variable_entry(our_variable, t_model):
            x_equal_list = []
            for i in range(len(our_variable)):
                x_equal_list.append(a + (b - a) * our_variable[i])
            t_list_incoming = [x_equal_list[0]]
            for i in range(1, len(x_equal_list) - 1):
                if x_equal_list[i] + t_list_incoming[-1] < t_model:
                    t_list_incoming.append(x_equal_list[i] + t_list_incoming[-1])
                else:
                    break
            return t_list_incoming, x_equal_list

        def getting_t_variable_maintenance(l):
            x_indicative_list = []
            if lyamda > 0:
                for i in range(len(our_variable)):
                    x_indicative_list.append((-1 / lyamda) * mt.log(our_variable[i]))
            t_list_maintenance = [x_indicative_list[0]]
            for i in range(1, l):
                t_list_maintenance.append(x_indicative_list[i])
            return t_list_maintenance

        def getting_t_variable_waiting(l):
            result = []
            for i in range(l):
                s = sum(our_variable[i:i + 12])
                result.append(myu + sigma * (s - 6))
            t_list_waiting = []
            for i in range(0, l):
                t_list_waiting.append(result[i])
            return t_list_waiting

        def diagram(count, comingTime, serviceTime, waitTime):
            countOfServiced, countOfRejected = 0, 0
            free = [0]
            Time_of_serviced = []
            for j in range(count):
                if comingTime[j] + waitTime[j] >= min(free) and comingTime[j] + serviceTime[j] <= t_model:
                    print(f"Client {j + 1} was serviced at {free.index(min(free)) + 1}")
                    free[free.index(min(free))] = comingTime[j] + serviceTime[j]
                    countOfServiced += 1
                    Time_of_serviced.append(serviceTime[j])
                else:
                    countOfRejected += 1
                    print(f"Client {j + 1} was rejected")
            return countOfRejected, countOfServiced, Time_of_serviced

        print(f"Experiments laws is {i}")
        T_variables_incoming, taos = getting_t_variable_entry(our_variable, t_model)
        l = len(T_variables_incoming)
        print("taos=", taos)
        print("T_variables_incoming=", T_variables_incoming)
        T_variables_maintenance = getting_t_variable_maintenance(l)
        print("T_variables_maintenance=", T_variables_maintenance)
        T_variables_waiting = getting_t_variable_waiting(l)
        print("T_variables_waiting=", T_variables_waiting)
        Count_of_rejected, Count_of_servised, Time_of_serviced = diagram(l, T_variables_incoming,
                                                                         T_variables_maintenance,
                                                                         T_variables_waiting)

        service_list.append(Count_of_servised / l)
        rejected_list.append(1 - (Count_of_servised / l))
        average_list.append(sum(Time_of_serviced) / Count_of_servised)
        bandwidth.append(Count_of_servised / sum(Time_of_serviced))
        print("Service-Probability = ", Count_of_servised / l, "\n")
        print("Reject-Probability = ", 1 - (Count_of_servised / l), "\n")
        print("Service-average-time = ", sum(Time_of_serviced) / Count_of_servised, "\n")
        print("Service bandwidth = ", Count_of_servised / sum(Time_of_serviced), "\n")
        print("Our_service = ", service_list, '\n')
        print("Our_reject = ", rejected_list, '\n')
        print("Our_average = ", average_list, '\n')
        print("Our_bandwidth = ", bandwidth, '\n')


def Student(service_list):
    N = len(service_list)
    P_mijin = sum(service_list) / N
    M_P = service_list[-1]
    value = 0
    for i in range(len(service_list)):
        value += (P_mijin - service_list[i]) ** 2
    sigma_P = mt.sqrt(value / (N - 1))
    t_hat = ((P_mijin - M_P) * mt.sqrt(N)) / sigma_P
    return abs(round(t_hat, 2)), sigma_P


def epsilon():
    return (1.66 * Sigma) / mt.sqrt(N)


a = 4
b = 8
lyamda = 0.6
myu = 7
sigma = 2
printing(a, b, lyamda, myu, sigma)
Styudent, Sigma = Student(service_list)
Epsilon = epsilon()
print("T_hat = ", Styudent, "\n")
print("Sigma = ", Sigma, "\n")
print("Epsilon = ", Epsilon, "\n")
