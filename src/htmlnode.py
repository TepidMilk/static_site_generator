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
    
class LeafNode(HTMLNode):
    #doesn't allow for children argument
    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag}{self.prop_to_html()}>{self.value}</{self.tag}>'