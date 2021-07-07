import time

#==STEP : 1==============================================
def s1_outer_fn_1():
    # why do we need inner functions?
    def inner_fn_1():
        print("i am the inner. Am i useless?")
    
    print("i am the outer. i don't know why i created the inner")
#==STEP : 2==============================================
def s2_outer_fn_2():
    # why do we need inner functions?
    def inner_fn_2():
        print("i am the inner 2. Use me")
    
    print("i am the outer 2, i use inner 2")
    inner_fn_2();
#==STEP : 3==============================================
def s3_greetings(username):
    def when_we_meet():
        print("hello "+ username)

    when_we_meet();   
#==STEP : 4==============================================
# how do we handle two inner functions
def s4_greetings(username):
    def when_we_meet():
        print("hello "+ username)
    def when_we_leave():
        print("bye " + username)

    when_we_leave();   
#==STEP : 5==============================================
# can we return inner functions, 
# after all python funcs are first class
# ok, let us return one function
def s5_greetings(username):
    def when_we_meet():
        print("hello "+ username)
    def when_we_leave():
        print("bye " + username)

    return when_we_meet   
    # how do we handle two inner functions
#==STEP : 6==============================================
# can we return more than one inner functions, 
# ok, let us return a dictionary of functions
def s6_greetings(username):
    def when_we_meet():
        print("hello "+ username)
    def when_we_leave():
        print("bye " + username)

    return {
        "meet": when_we_meet, 
        "leave": when_we_leave
        }   
#==STEP : 7==============================================
# ok, so we can save some state, like a tiny object
# let's see if we can say greetings in different languages
def s7_greetings(lang, username):
    # default  : english
    meet = "hello "
    leave = "bye "
    
    if lang == "english": 
        meet = "hello "
        leave = "bye " 
    elif lang == "spanish": 
        meet = "hola "
        leave = "adios " 
    elif lang == "hawaian":
        meet = "aloha "
        leave = "aloha "
    
    
    def when_we_meet():
        print(meet + username)
    def when_we_leave():
        print(leave + username)

    return {
        "meet": when_we_meet, 
        "leave": when_we_leave
        }   
#==STEP : 8==============================================
# maybe build a common day to day usage example
# lecture rooms with digital doors that provide 
# us with no of people inside
def lecture_room():

    people_count = 0;

    def enter(people):
        # pyton 3 introduced nonlocal
        # if you get illegal syntax for nonlocal , 
        # check to make sure your compiler is 3.x +
        # https://stackoverflow.com/questions/2609518/unboundlocalerror-with-nested-function-scopes
        nonlocal people_count
        people_count+=people

    def leave(people):
        nonlocal people_count
        people_count-=people

    def occupancy():
        return people_count

    def empty_the_room():
        # achtung: be careful
        # make sure you don't end up modifying
        # local variables in the function
        nonlocal people_count
        people_count = 0

    return {
        "enter": enter,
        "leave": leave,
        "occupancy": occupancy,
        "empty_the_room": empty_the_room
    }

def test_lecture_rooms():

    rm_201 = lecture_room()
    rm_202 = lecture_room()

    rm_201["enter"](30)
    rm_202["enter"](10)

    rm_201["leave"](1)
    rm_202["leave"](6)

    print(rm_201["occupancy"]()) # 3 - 1 = 2
    print(rm_202["occupancy"]()) # 10 - 6 = 4

    rm_201["empty_the_room"]()
    print(rm_201["occupancy"]()) # should be 0

#==STEP : 9==============================================
# decorators, call before and after
# @decorator
# def decorated_func():
#   pass
# does the following
# decorated_func = decorator(decorated_func)

def addmessages(func):
    def _inner_working():
        print("I execute before")
        func()
        print("I execute after")
    return _inner_working

@addmessages
def greet_decorators():
    print("hello decorators")

def execution_time(func):
    def _clock_it():
        # start clock
        tic = time.perf_counter()
        # execute func
        func()
        # end clock
        toc = time.perf_counter()
        # print time taken
        print(f"time taken: {toc - tic:0.4f} seconds")
    # if you get following error, make sure you return a func
    # TypeError: 'NoneType' object is not callable
    return _clock_it

def this_func_is_not_doing_anything_yet():
    # but it has potential!
    pass

@execution_time
def time_me_i_sleep_for_2_seconds():
    print("going to nap for 2 seconds")
    time.sleep(2)
    print("good nap!")

# execution_time(time_me_i_sleep_for_2_seconds)
    

#================================================
# main entry point
def main():
    # print("hello python!")
    # s1_outer_fn_1()
    # # ok, how do we get to execute inner fn
    # s2_outer_fn_2()
    # # write some sensible code, not foos and bars
    # s3_greetings("jay")  
    # s4_greetings("shailesh")
    # # return inner functions
    # s5_g = s5_greetings("duong")
    # s5_g()
    # # return more than one
    # s6_d = s6_greetings("vincent")
    # at this point s6_greeting should not be on stack
    # then how come the parameter 'vincent' 
    # is still accessible????
    # s6_d["meet"]() # hello vincent
    # s6_d["leave"]() # bye vincent
    # # different languages
    # two separate invocations
    # s7_d = s7_greetings("spanish", "lejing")
    # s7_d["meet"]()
    # s7_d["leave"]()
    # s7_d1 = s7_greetings("hawaian", "ife")
    # s7_d1["meet"]()
    # s7_d1["leave"]()
    # # lecture rooms
    # test_lecture_rooms()
    # # decorators
    # greet_decorators()
    # time_me_i_sleep_for_2_seconds()
#================================================
# let's start
main()

#================================================
# good reads
# https://realpython.com/inner-functions-what-are-they-good-for/#retaining-state-with-inner-functions-closures
# https://realpython.com/python-timer/
# https://realpython.com/inner-functions-what-are-they-good-for/#adding-behavior-with-inner-functions-decorators