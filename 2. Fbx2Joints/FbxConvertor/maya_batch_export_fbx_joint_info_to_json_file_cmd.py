# -*- coding: utf-8 -*-

import os
import json
import codecs
import sys

import maya.cmds as cmds
import maya.standalone
maya.standalone.initialize()

root_joint_name = "m_avg_root"

def get_changed_extention_abs_path(abs_path,ext):
    return os.path.splitext(abs_path)[0]+"."+ext.replace(".","")

def set_currentTime_to_playback_start_time():
    cmds.currentTime(cmds.playbackOptions(q=True, min=True))

def load_plugin(plugin_name):  # fbxmaya.mll
    if not cmds.pluginInfo(plugin_name, q=True, loaded=True):
        cmds.loadPlugin(plugin_name)

def main(fbx_folder_path):
    '''{
        "file_basename":"a103_030000.fbx",
        "frame_length":53,
        "frame_sequence":[
            {
                "frame_number" : 0,
                "joint_name": "Master",
                "position_x": "1",
                "position_y": "2",
                "position_z": "3"
            }
        ]
    }'''

    '''{
        "file_basename":"a103_030000.fbx",
        "frame_length":53,
        "frame_sequence":[
            {
                "frame_number" : 0,
                "joint_position" : [
                    {
                        "joint_name": "Master",
                        "position_x": "1",
                        "position_y": "2",
                        "position_z": "3"
                    }
                ]
            }
        ]
    }'''
    fbx_count=0
    for index, fbx_basename in enumerate(os.listdir(fbx_folder_path)):
        fbx_abs_path=os.path.join(fbx_folder_path,fbx_basename)
        # fbx_basename_no_extension=os.path.splitext(fbx_basename)[0]
        if os.path.isfile(fbx_abs_path) and fbx_abs_path.endswith(".fbx"):
            fbx_count+=1
            print ("current fbx:", fbx_count)
            print ("fbx_abs_path", fbx_abs_path)

            cmds.file(new=True, force=True)
            cmds.file(fbx_abs_path, open=True)

            start_joint = root_joint_name
            cmds.select(start_joint)
            allDescendents = cmds.listRelatives(allDescendents=True, type='joint')  # priority depth traversal
            allDescendents.append(start_joint) # That's it
            allDescendents.reverse()

            min_time = int(cmds.playbackOptions(q=True, min=True))
            max_time = int(cmds.playbackOptions(q=True, max=True)) ## cmds.playbackOptions(q=True, max=True) Result: 66.0 #
            frame_length = max_time - min_time + 1
            joint_dic = {
                u"file_basename": fbx_basename,
                u"frame_length": frame_length,
                u"frame_sequence": []
            }
            for currentTime in range(min_time,max_time+1):
                cmds.currentTime(currentTime)

                join_pos_dic_list=[]
                for i, joint in enumerate(allDescendents):
                    pos = cmds.xform(joint, q=True, t=True, ws=True)
                    rot = cmds.xform(joint, q=True, ro=True) # relative rotation
                    join_pos_dic_list.append({
                            "joint_name": joint,
                            "position_x": pos[0],
                            "position_y": pos[1],
                            "position_z": pos[2],
							"rotation_x": rot[0],
							"rotation_y": rot[1],
							"rotation_z": rot[2],
                        })
                joint_dic[u"frame_sequence"].append({
                    u"frame_number": currentTime,
                    u"joint_position": join_pos_dic_list
                })
            with open(get_changed_extention_abs_path(fbx_abs_path,".json"), "w") as f:
                json.dump(joint_dic, f, indent=4)

            # with codecs.open(get_changed_extention_abs_path(fbx_abs_path,".json"), "w", 'utf-8') as f:
            #     json.dump(joint_dic, f, indent=4)

            # f = codecs.open(get_changed_extention_abs_path(fbx_abs_path,".json"), 'w', 'utf-8')
            # f.write(json.dumps(joint_dic, indent=4)) #\u5e27\u5e8f\u5217
            # f.close()

            # if fbx_count ==3:
            #     return

if __name__ == "__main__":
    load_plugin("fbxmaya.mll")
    fbx_folder_path = sys.argv[1]
    # main(r"D:\Project\PycharmProjects\maya\!paid_scripts\batch_export_fbx_joint_info_to_json_file\test\ref\fbx")
    # "C:\Program Files\Autodesk\Maya2019\bin\mayapy.exe" "C:\Users\admin\PycharmProjects\maya\self_made\use_cmd_export\main_cmd.py" "Z:\WORK_ROOT\WorksRoot\Animas\SC009_weiyi\GB_SC009_shot0020_023_ani.ma" -a -o "C:\Users\admin\Desktop"
    main(fbx_folder_path)
