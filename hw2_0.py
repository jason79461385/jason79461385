def hw2_0(rows=3):
    output = ''
    # ======請在這個區域寫程式=====
    current_num=0
    counter=0
    output=""
    while current_num<=int(rows)-1:
        space=0
        while space<int(rows)-counter-1:
            output=output+str(" ")
            space=space+1
        star=0
        while star<(current_num+1):
            output=output+str("*")
            star=star+1
            if star<(current_num+1):
                output=output+str(" ")
        current_num=current_num+1
        if current_num!=int(rows):
            output=output+str("\n")
        counter=counter+1
    # ============================
    return output
