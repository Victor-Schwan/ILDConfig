from TrackingReco_FCCeeMDI import conformal_tracking_steps_config
from TrackingReco_FCCeeMDI_old import old_CT_param_list
from tracking_utils import encode_CT_steps_dict_to_legacy_list

new_list = encode_CT_steps_dict_to_legacy_list(conformal_tracking_steps_config)

print("new   |   old")


for el_new, el_old in zip(new_list, old_CT_param_list):
    if not el_new == el_old:
        print(f"{el_new} {el_old}")