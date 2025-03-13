import sys

args_dict = {}

to_sorting = False
for arg in sys.argv[1:]:
    if arg == '--sort':
        to_sorting = True
        continue

    key, value = arg.split('=')
    args_dict[key] = value

if to_sorting:
    args_dict = {key: args_dict[key] for key in sorted(args_dict.keys())}

for key in args_dict.keys():
    print(f'Key: {key} Value: {args_dict[key]}')
