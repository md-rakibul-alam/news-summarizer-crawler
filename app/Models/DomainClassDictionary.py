class DomainClassDictionary:
    @staticmethod
    def get(domain_name):
        domain_class_mapping = {
            "prothomalo.com": "story-element story-element-text",
            "dailyamardesh.com": "text-xl leading-8 text-black my-8 story-details",
            # Add more domain to class mappings as needed
        }
        return domain_class_mapping.get(domain_name)