# The mail.txt file is supposed to be formatted as follow:

# Richard Feynman <rich@caltech.edu>,
# ...
# <iforgotthisguysnamebutihavehisemail@gmail.com>,
# Elon Musk <elon.musk@tesla.com>

lines = [line.rstrip('\n').rstrip(',').split() for line in open('mail.txt')]

for line in lines:
    print(line)

with open('google_contacts.csv', 'w') as f:

    # write the name of the columns for the google contacts csv file
    f.write("Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,E-mail 1 - Type,E-mail 1 - Value,E-mail 2 - Type,E-mail 2 - Value,Phone 1 - Type,Phone 1 - Value,Phone 2 - Type,Phone 2 - Value,Phone 3 - Type,Phone 3 - Value,Address 1 - Type,Address 1 - Formatted,Address 1 - Street,Address 1 - City,Address 1 - PO Box,Address 1 - Region,Address 1 - Postal Code,Address 1 - Country,Address 1 - Extended Address,Organization 1 - Type,Organization 1 - Name,Organization 1 - Yomi Name,Organization 1 - Title,Organization 1 - Department,Organization 1 - Symbol,Organization 1 - Location,Organization 1 - Job Description\n")

    for line in lines:

        # if no first name or last name, then blank in csv
        first_name = ""
        last_name = ""
        full_name = ""

        # in gmail, emails are the last field, as "<elon.musk@tesla.com>"
        # so we need to take the last element and get rid of those "<" and ">"
        print("line[-1] is: |", line[-1], "|")
        mail = line[-1][1:-1]
        print("mail is:" + mail)

        # if no names are provided (only mail), the len of "line" is only 1
        if (len(line) >= 3):
            first_name,last_name = line[0], line[1]
            full_name = first_name + " " + last_name
        # constructing a string compatible with the Google Contacts format
        # e.g. Elon Musk,Elon,,Musk,,,,,,,,,,,,,,,,,,,,,,,,,,* ,elon.musk@tesla.com,,,,,,,,,,,,,,,,,,,,,,,,,
        string_for_csv = full_name + "," + first_name + ",," + last_name + \
                            26 * "," + "* ," + mail + 25 * "," + '\n'
        f.write(string_for_csv)
        print(string_for_csv)
