import os

def Test():
    print("Test")

    directory_original_str = "redirections/flowvis-tool/pacificvis3"
    directory_target_str = "redirections/flowvis-tool/pacificvis4"
    directory_target_local_str = "redirections/flowvis-tool/pacificvis4_local"
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
                    value = "2"

                #SET VERSION MONTH TO 2
                if(key == "v_m"):
                    value = "2"

                #SET VERSION YEAR TO 2024
                if(key == "v_y"):
                    value = "2024"

                #skip completion marker
                if(key == "c"):
                    continue

                if not is_first:
                    new_parameters += "&"
                new_parameters += key + "=" + value
                is_first = False


            #new_parameters += "&" + "chris" + "=" + "0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0~0"
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