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

    directory_original_str = "redirections/flowvis-tool/pacificvis"
    directory_target_str = "redirections/flowvis-tool/pacificvis2"
    directory_target_local_str = "redirections/flowvis-tool/pacificvis2_local"
    directory_original = os.fsencode(directory_original_str)
    directory_target = os.fsencode(directory_target_str)

    for file in os.listdir(directory_original):
        filename = os.fsdecode(file)
        file_path = os.path.join(directory_original_str, filename)
        file_path_out = os.path.join(directory_target_str, filename)
        file_path_out_local = os.path.join(directory_target_local_str, filename)
        
        print("")
        print("file_path:", file_path)
        with open(file_path) as f:
            content = f.read()

            #url_without_parameters = content.split("?")[0]
            url_without_parameters = "https://sfb-trr191.github.io/3-torus-flowvis-tool/index.html"
            url_local_without_parameters = "http://localhost:8000/index.html"
            parameters = content.split("?")[1]

            list_pair_strings = parameters.split("&")

            new_parameters = ""
            is_first = True

            has_manifold_formulation = False
            has_flow_formulation = False
            converted_space_to_manifold_formulation = "0"
            converted_space_to_flow_formulation = "0"

            for s in list_pair_strings:    
                key = s.split("=")[0]
                value_original = s.split("=")[1]   
                value = value_original

                #SET VERSION NUMBER TO 1
                if(key == "v_n"):
                    value = "1"

                #SET VERSION MONTH TO 10
                if(key == "v_m"):
                    value = "11"

                #skip completion marker
                if(key == "c"):
                    continue

                if not is_first:
                    new_parameters += "&"
                new_parameters += key + "=" + value
                is_first = False


            new_parameters += "&" + "chris" + "=" + "0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0"
            #add completion marker
            new_parameters += "&c=1"

            #write to new_parameters file
            #print("new_parameters", new_parameters)
            print("file_path_out:", file_path_out)
            with open(file_path_out, "w") as f_out:
                f_out.write(url_without_parameters + "?" + new_parameters)


            with open(file_path_out_local, "w") as f_out:
                f_out.write(url_local_without_parameters + "?" + new_parameters)


            


if __name__ == '__main__':
    print("start")
    Test()