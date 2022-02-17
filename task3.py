def mathclub():
   first_class = int(input("Pupils at 1`st classroom: "))
   second_class = int(input("Pupils at 2`st classroom: "))
   third_class = int(input("Pupils at 3`st classroom: "))
   desk_for_first = int((first_class / 2)) + (first_class % 2)
   desk_for_second = int((second_class / 2)) + (second_class % 2)
   desk_for_third = int((third_class / 2)) + (third_class % 2)
   print("Desk`s for 1`st classroom: ", desk_for_first)
   print("Desk`s for 2`st classroom: ", desk_for_second)
   print("Desk`s for 3`st classroom: ", desk_for_third)
   need_desk = desk_for_second + desk_for_third + desk_for_first
   print("For all classrooms need ", need_desk, "desk`s")
mathclub()



