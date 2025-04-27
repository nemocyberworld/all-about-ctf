import hashlib
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = "}"
temp = hashlib.sha256(b"FREEMAN").hexdigest()
key_part_dynamic1_trial = temp[4] + temp[5] + temp[3] + temp[6] + temp[2] + temp[7] + temp[1] + temp[8]
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(key_full_template_trial)