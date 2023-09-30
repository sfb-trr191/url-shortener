import os

def ReplaceSymbols(value):
    #empty space removal
    value = value.replace("%20", "")
    #double pendulum
    value = value.replace("v_x", "v1")
    value = value.replace("v_y", "v2")
    #3-torus
    value = value.replace("x", "x1")
    value = value.replace("y", "x2")
    value = value.replace("z", "x3")
    #sphere
    value = value.replace("p0", "x1")
    value = value.replace("p1", "x2")
    value = value.replace("p2", "x3")
    value = value.replace("p3", "x4")

    value = value.replace("d0", "v1")
    value = value.replace("d1", "v2")
    value = value.replace("d2", "v3")
    value = value.replace("d3", "v4")
    return value    

def ReplaceSymbolsRule(value):
    #empty space removal
    value = value.replace("%20", "")
    #direction
    value = value.replace("v", "v2")#needs to be first
    value = value.replace("u", "v1")
    value = value.replace("w", "v3")
    #direction
    value = value.replace("x", "x1")
    value = value.replace("y", "x2")
    value = value.replace("z", "x3")
    return value    

def Test():
    print("Test")
    list_keys_containing_symbols = [
        "u", "v", "w",#3-torus
        "a", "b",#double pendulum
        "fs",#formular scalar
        "p0", "p1", "p2", "p3", "d0", "d1", "d2", "d3",#sphere
        "lp0", "lp1", "lp2", "lp3", "ld0", "ld1", "ld2", "ld3"#light integration
        ]
    list_keys_rule = [
        "rxpx", "rxpy", "rxpz", "rxnx", "rxny", "rxnz",
        "rypx", "rypy", "rypz", "rynx", "ryny", "rynz",
        "rzpx", "rzpy", "rzpz", "rznx", "rzny", "rznz",
        "rxpu", "rxpv", "rxpw", "rxnu", "rxnv", "rxnw",
        "rypu", "rypv", "rypw", "rynu", "rynv", "rynw",
        "rzpu", "rzpv", "rzpw", "rznu", "rznv", "rznw",
    ]

    directory_original_str = "redirections/flowvis-tool/pacificvis_old"
    directory_target_str = "redirections/flowvis-tool/pacificvis"
    directory_original = os.fsencode(directory_original_str)
    directory_target = os.fsencode(directory_target_str)

    for file in os.listdir(directory_original):
        filename = os.fsdecode(file)
        file_path = os.path.join(directory_original_str, filename)
        file_path_out = os.path.join(directory_target_str, filename)
        print("file_path:", file_path)
        with open(file_path) as f:
            print("")
            content = f.read()

            url_without_parameters = content.split("?")[0]
            parameters = content.split("?")[1]

            list_pair_strings = parameters.split("&")

            new = url_without_parameters + "?"
            is_first = True
            for s in list_pair_strings:    
                key = s.split("=")[0]
                value_original = s.split("=")[1]   
                value = value_original

                if(key in list_keys_containing_symbols):
                    value = ReplaceSymbols(value_original)
                    print("key", key, "value:", value, "old:", value_original)
                if(key in list_keys_rule):
                    value = ReplaceSymbolsRule(value_original)
                    print("key", key, "value:", value, "old:", value_original)

                    

                #SET VERSION NUMBER TO 2
                if(key == "v_n"):
                    value = "2"

                if not is_first:
                    new += "&"
                new += key + "=" + value
                is_first = False
            
            #write to new file
            print("new", new)
            print("file_path_out:", file_path_out)
            with open(file_path_out, "w") as f_out:
                f_out.write(new)


            


if __name__ == '__main__':
    print("start")
    Test()