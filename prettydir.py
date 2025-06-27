import sys
import importlib

def main():
    path = {"classes": [],
            "attributes": [],
            "methods": [],
            "dunder": []}
    module = importlib.import_module(sys.argv[1])
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