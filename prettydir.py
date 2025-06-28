import sys
import importlib

def get_module(name):
    try:
        module = importlib.import_module(name)
    except ModuleNotFoundError:
        raise ModuleNotFoundError("check if the module is installed and try again!")
    return module

def main():
    module = get_module(sys.argv[1])

    path = {"classes": [],
            "attributes": [],
            "methods": [],
            "dunder": []}
    contents = [name for name in dir(module) if callable(getattr(module, name))]
    path['attributes'] = [name for name in dir(module) if not callable(getattr(module, name))]
    with open('directory.txt', 'w') as directory_file:
        classes, methods, dunder = [], [], []
        for content in contents:
            if content.startswith('_'):
                path['dunder'].append(content)
            if content[0].isupper():
                path['classes'].append(content)
            else:
                path['methods'].append(content)

        for key, value in path.items():
            directory_file.write(key + '- \n')
            for val in value:
                directory_file.write(val + '\n')
            directory_file.write('\n')

if __name__ == "__main__":
    main()