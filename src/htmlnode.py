class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    #to be inherited
    def to_html(self):
        raise NotImplementedError
    
    #Convert prop constructor dictionary into a single line string where each key value pair is converted to html format
    def prop_to_html(self):
        final_string = ""
        for atr in self.props:
            string_add = f'{atr}="{self.props[atr]}"'
            final_string += " " + string_add
        return final_string
    
    #string representation of constructors
    def __repr__(self):
        return (f"tag: {self.tag}, value: {self.value} children: {self.children}, props: {self.props}")
    
    def __eq__(self):
        raise NotImplementedError
    

#handles HTMLNodes with no children
class LeafNode(HTMLNode):
    #doesn't allow for children argument
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag}{self.prop_to_html()}>{self.value}</{self.tag}>'
    
    def __eq__(self, node2):
        if self.value != node2.value:
            raise Exception(f"{self.value} does not equal {node2.value}")
        elif self.tag != node2.tag:
            raise Exception(f"{self.tag} does not equal {node2.tag}")
        elif self.props != node2.props:
            raise Exception(f"{self.props} does not equal {node2.props}")
        return True
#handles HTMLNodes nesting within each other
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No Tag")
        if self.children == None:
            raise ValueError("No Children")
        result = ""
        for child in self.children:
            result += child.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"
    
    def __eq__(self, node2):
        if self.value != node2.value:
            raise Exception(f"{self.value} does not equal {node2.value}")
        elif self.tag != node2.tag:
            raise Exception(f"{self.tag} does not equal {node2.tag}")
        elif self.props != node2.props:
            raise Exception(f"{self.props} does not equal {node2.props}")
        return True