def main():
    """
    ##################################################
    Complete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    
    m_num = int(input("Enter the number of males in your class: "))
    f_num = int(input("Enter the number of females in your class: "))
    total = m_num + f_num
    m_perc = 100*m_num/total
    f_perc = 100*f_num/total

    print(f'The total number of students: \t \t {total}')
    print(f'The number of males and females \t {m_num} \t {f_num}')
    print(f'The percentage of males and females \t {m_perc:.2f}%  {f_perc:.2f}%')

    # my GitHub Link: https://github.com/LPC-CSDept/assignment-2-1-aliahmergtr





    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
