import re


def parse_tex(file, config):
    # rule = re.compile(r'\\begin{equation}(.*?)\\end{equation}',re.S)
    # with open(file, 'rb') as f:
    #     content = f.read().decode('utf-8')
    #     content = content.replace('\n','')
    #     results = rule.findall(content)
    # return results
    pass

def remove_annotations(file_path):
    """
    移除`.tex`中的注释。
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    no_annotation = ''.join([line for line in lines if line.strip() != "" and not line.startswith("%")])
    return no_annotation

def remove_environment(content, environment_name):
    """
    
    """
    pattern = r'\\begin{' + environment_name + r'}.*?\\end{' + environment_name + r'}'
    modified_content = re.sub(pattern, '', content, flags=re.DOTALL)
    return modified_content

def get_section_names(content):
    section_pattern = r'\\section{(.*?)}'
    return re.findall(section_pattern, content)

def get_subsection_names(content):
    subsection_pattern = r'\\section{(.*?)}'
    return re.findall(subsection_pattern, content)


if __name__ == "__main__":
    no_annotations = remove_annotations(r"test-folder\2010.01815\main.tex")
    no_environments = remove_environment(no_annotations, "equation")
    
    
