class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def prop_to_html(self):
        final_string = ""
        for atr in self.props:
            string_add = atr.key + "=" + atr.value
            final_string += " " + string_add
        return final_string
    
    def __repr__(self):
        return (f"tag: {self.tag}, value: {self.value} children: {self.children}, props: {self.props}")
    
