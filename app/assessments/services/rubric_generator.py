from .taxonomy import TAXONOMY
from .descriptor_templates import DESCRIPTOR_TEMPLATES
from .skill_map import SKILL_MAP

OUTCOME_CRITERIA_MAP = {
    "EN11-1": [
        "Communication",
        "Project progression",
        "Testing methodology",
        "Project Solution",
        "Understanding of the system",
        "Optimisations of the system",

    ]
}

#OUTCOME_CRITERIA_MAP = {
#   "EN11-1": [
#       "Demonstrates project progression and problem-solving through documented evidence",
#       "Communication",
#       "Demonstrates a testing methodology",
#       "Project Solution",
#       "Demonstrates an understanding of the system created, how it works and key parts of the code",
#       "Explains optimisations of the systems, focusing on iterations from the prototype",
#        "Communication",
#    ]
#}

def generate_rubric(selected_outcomes):

    criteria = []

    for outcome in selected_outcomes:

        if outcome in OUTCOME_CRITERIA_MAP:
            criteria.extend(
                OUTCOME_CRITERIA_MAP[outcome]
            )

    criteria = list(set(criteria))

    rubric = {}

    for criterion in criteria:

        rubric[criterion] = {}

        template = DESCRIPTOR_TEMPLATES[criterion]

        skill = SKILL_MAP[criterion]

        for band, quality in TAXONOMY.items():

            descriptor = template.format(
                quality=quality,
                skill=skill
            )

            rubric[criterion][band] = descriptor

    return rubric