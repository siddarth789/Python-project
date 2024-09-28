import time
from threading import Timer

rooms = {i: None for i in range(1, 31)}
act_t = []


def main():
    while True:
        print(" ")
        print("1. Add room and allocate student")
        print("2. Show rooms")
        print("3. Exit")
        c = input("Enter your choice: ")
        if c == '1':
            rid = int(input("Enter the room id: "))
            addrm(rid)
        elif c == '2':
            show_rooms()
        elif c == '3':
            print("Exiting the program.")
            can_t()
            break

def addrm(rid):
    if rid > 30:
        print("Rooms are only up to 30.")
        return

    if rooms[rid] is not None:
        print(f"Room {rid} is already occupied by another student.")
        fi_room = next((r for r, v in rooms.items() if v is None), None)
        if fi_room:
            print("____--____")
            print(f"Allocating student to another available room: {fi_room}")
            sid = input("Enter the student ID: ")

            if st_in_rm(sid):
                print(f"Student {sid} is already allocated to another room.")
                return
            etime = time.time()
            for_etime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(etime))
            rooms[fi_room] = (sid, etime)
            print(f"Room {fi_room} allocated to Student {sid} at {for_etime} for 2 minutes.")
            t= Timer(120, re_st, [fi_room])
            t.start()
            act_t.append(t)

        else:
            print("Sorry, all rooms are currently occupied.")
    else:
        sid = input("Enter the student ID: ")

        if st_in_rm(sid):
            print(f"Student {sid} is already allocated to another room.")
            return
        etime = time.time()
        for_etime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(etime))
        rooms[rid] = (sid, etime)
        print(f"Room {rid} allocated to Student {sid} at {for_etime} for 2 minutes.")
        t = Timer(120, re_st, [rid])
        t.start()
        act_t.append(t)


def st_in_rm(sid):
    return any(i and i[0] == sid for i in rooms.values())


def re_st(rid):
    sid, etime = rooms[rid]
    dura = time.time() - etime
    for_etime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(etime))
    print(" ")
    print(f"\nRoom {rid} has been freed from Student {sid}.")
    print(f"Student {sid} entered the room at {for_etime} and spent {dura / 60:.2f} minutes in the room.")
    rooms[rid] = None


def show_rooms():
    for rid, info in rooms.items():
        if info:
            sid, etime = info
            for_etime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(etime))
            print(f"room {rid}: occupied by Student {sid} (since {for_etime})")
        else:
            print(f"Room {rid}: Empty")

def can_t():
    for t in act_t:
        t.cancel()
    print("all timers are has been cancelled")

main()
