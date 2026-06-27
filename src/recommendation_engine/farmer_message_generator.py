"""
Farmer Message Generator

Converts recommendation records into
farmer-friendly readable messages.
"""


class FarmerMessageGenerator:

    def generate_disease_message(self, recommendation):

        if recommendation["status"] != "success":
            return self.generate_unknown_message()

        message = f"""
========================================
DISEASE DETECTED
========================================

Disease Name:
{recommendation['disease_name']}

Severity:
{recommendation['severity_level']}

Description:
{recommendation['description']}

Treatment:
{recommendation['treatment']}

Organic Treatment:
{recommendation['organic_treatment']}

Chemical Treatment:
{recommendation['chemical_treatment']}

Preventive Measures:
{recommendation['preventive_measures']}

Monitoring Actions:
{recommendation['monitoring_actions']}
"""

        return message

    def generate_pest_message(self, recommendation):

        if recommendation["status"] != "success":
            return self.generate_unknown_message()

        message = f"""
========================================
PEST DETECTED
========================================

Pest Name:
{recommendation['pest_name']}

Scientific Name:
{recommendation['scientific_name']}

Damage Severity:
{recommendation['damage_severity']}

Description:
{recommendation['description']}

Organic Control:
{recommendation['organic_control']}

Chemical Control:
{recommendation['chemical_control']}

Prevention Measures:
{recommendation['prevention_measures']}

Monitoring Actions:
{recommendation['monitoring_actions']}
"""

        return message

    def generate_unknown_message(self):

        return """
========================================
RECOMMENDATION NOT AVAILABLE
========================================

No recommendation was found.

Please:

1. Upload a clearer image.
2. Verify crop or pest identification.
3. Consult an agricultural expert.
"""