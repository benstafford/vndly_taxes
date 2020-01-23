import re

class Scanner:
    
    @staticmethod
    def scan(items):
        # "1 book at 12.49"
        pattern = re.compile(r'(?P<quantity>\d+) (?P<item>.*) at (?P<price>\d+\.\d+)')
        
        return [re.match(pattern, item).groupdict() for item in items]
