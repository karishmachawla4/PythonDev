try:
    user_name = input("Please enter your username")
    pass_word = input("Enter your password here")
    re_pass = input("Renter your password")
    cnt = 1
    while cnt <= 3:
        if pass_word != re_pass:
            print(" Your password does not match, Re-try again ", cnt)
            pass_word = input("Enter your password here again")
            re_pass = input("Renter your password again")
            cnt += 1
        else:
            print(" Your are successfully logged in")
            break

    if cnt == 4:
        print(" Your account is temporarily locked")
        print("Please try to login again later")
except:
    print(" Syntax error")