def generate_emails(base_email, num_emails, campus):
    """
    Generates a list of emails based on a base email, an email count and campus
    """
    
    base_value = 501 if campus == "nc" else 1
    
    if campus == "nc":
        for i in range(num_emails):
            print(base_email + str(i + base_value) + "@pucit.edu.pk,", end=" ")
    else:
        for i in range(num_emails):
            if i < 9:
                print(base_email + "00" + str(i + base_value) + "@pucit.edu.pk,", end=" ")
            else:
                print(base_email + "0" + str(i + base_value) + "@pucit.edu.pk,", end=" ")



if __name__ == '__main__':
    
    year = "18"
    campus = "nc"
    
    generate_emails('bsef' + year + 'm' , 45, campus)
    generate_emails('bsef' + year + 'a' , 45, campus)
    generate_emails('bcsf' + year + 'm' , 45, campus)
    generate_emails('bcsf' + year + 'a' , 45, campus)
    generate_emails('bitf' + year + 'm' , 45, campus)
    generate_emails('bitf' + year + 'a' , 45, campus)
