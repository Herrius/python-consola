import pandas as pd

def dictionary():
    weather_c={
        "Monday":12,
        "Tuesday":14,
        "Wednesday":15,
        "Thursday":14,
        "Friday":21,
        "Saturday":22,
        "Sunday":24
    }

    farehenint={
        day:(temp*9/5+32) for day,temp in weather_c.items()
    }
    print(farehenint)

def pand():
    student_dict={
        "student":["Angela","James","Lily"],
        "score":[56,76,98]
    }
    # for(key,value) in student_dict.items():
    #     print(value)
    student_data_frame=pd.DataFrame(student_dict)
    print(student_data_frame)
    for(index,row) in student_data_frame.iterrows():
        print(row.student)
        print(row.score)

def main():
    pand()

main()