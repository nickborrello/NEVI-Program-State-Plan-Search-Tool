# Dictionary of every states name and abbreviation
states = {
    "AK": "Alaska",
    "AL": "Alabama",
    "AR": "Arkansas",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DC": "District of Columbia",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MS": "Mississippi",
    "MT": "Montana",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": "Nevada",
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VA": "Virginia",
    "VT": "Vermont",
    "WA": "Washington",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": "Wyoming",
}

# Dictionaries containing all of the questions and corresponding search terms for each category
# Equity category
equity = {
    # This is a question that users could select
    "What methods did the state employ to engage stakeholders in the development of the plan?":
    # Below are sets of words that hold similar meaning within each of the state plans, the answer to the question above will typically contain at least one word from each of the sets
    [
        # These are all words that relate to different groups of stakeholders that states might reach out to
        [
            "stakeholders",
            "communities",
            "members of",
            "members from",
            "individuals from",
            "representatives from",
            "leaders of",
            "leaders from",
        ],
        # These are terms addressing different ways that states could be engaging the stakeholders
        [
            "engage",
            "outreach",
            "contacted",
            "contacting",
            "collaborate",
            "build relationships",
            "engaging",
            "engagement",
            "building relationships",
            "public engagement",
        ],
        [
            # Space means these are not required terms
            " ",
            "focus groups",
            "events",
            "survey",
            "interview",
            "webinar",
            "outline platform",
            "partnership",
            "proposals",
            "coordination meeting",
            "presentation",
            "listening session",
            "informational session",
            "online public notices",
            "conference",
            "meeting",
        ],
    ],
    "How does the state identify disadvantaged communities?": [
        [
            "underserved",
            "underdeveloped",
            "disadvantaged",
            "DAC",
            "marginalized",
            "overburdened",
            "tribal",
        ],
        [
            "define",
            "defining",
            "definition",
            "identify",
            "identifying",
            "identification",
            "locate",
            "locating",
        ],
        [
            " ",
            "roundtable",
            "mapping tool",
            "equitability",
            "engagement",
            "outreach",
            "collaborate",
            "collaboration",
            "indicators",
            "factors",
        ],
    ],
    "What factors does the state impact assessment consider?": [
        ["factors", "factor"],
        ["consider"],
    ],
    "Does the state plan to prioritize applications that consider impacts to DACs?": [
        ["vendors", "third-party", "contractor", "partners", "projects"],
        [
            "underserved",
            "underdeveloped",
            "disadvantaged",
            "DAC",
            "equity",
            "engagement",
            "engage",
            "community",
            "communities",
        ],
        ["prioritize", "focus on", "select", "work with"],
    ],
    "What benefits/disbenefits to DACs are considered in the state plan?": [
        ["benefits", "benefit", "disbenefit", "disbenefits"],
        [
            "underserved",
            "underdeveloped",
            "disadvantaged communities",
            "DAC",
            "marginalized",
            "overburdened",
            "tribal",
        ],
    ],
}
buildout = {
    "Who will provide the 20% required match?": [
        ["20%", "20 percent", "80/20"],
        ["cost share", "match", "federal fund", "private fund", "private"],
    ],
    "What strategies does the state use to encourage EV workforce development?": [
        ["workforce", "contractors", "workers", "those hired"],
        ["training", "programs", "educate", "education"],
    ],
    "What strategies does the state use to ensure that people with disabilities can access charging stations?": [
        [
            "disabilities",
            "disability",
            "language barrier",
            "barriers",
            "languages",
            "accessibilty",
            "accessible",
            "multilingual",
            "lingual",
        ]
    ],
    "What factors did the state consider when designating new AFCs?": [
        ["AFC", "alternative fuel corridor", "corridors", "corridor"],
        [
            "newly",
            "designation",
            "nominate",
            "potential",
            "prioritize",
            "prioritization",
        ],
        ["amenities", "traffic", "evacuation", "existing", "connectivity"],
    ],
    "What factors does the state prioritize when selecting sites?": [
        ["sites", "projects"],
        ["prioritze", "score", "weight", "selecting", "choosing"],
    ],
    "How are states planning on engaging with existing off-highway infrastructure when deploying EV chargers?": [
        # Words that relate to off highway amenities
        [
            "off-highway infrastructure",
            "offhighway infrastructure",
            "amenities",
            "bathroom",
            "restaurant",
            "food",
            "restroom",
        ],
        # Words relating to pre-existing, allready in place
        [
            "existing",
            "established",
            "preexisting",
            "preestablished",
            "pre-established",
            "in-place",
        ],
    ],
    "How do states plan to respond to any environmental, geographical, or climate-based challenges in regards to the buildout of EV chargers?": [
        []
    ],
    "How does the state address accessibility and general safety at charging stations?": [
        []
    ],
    "How are on site renewable energy resources for charging stations being considered?": [
        []
    ],
}
maintenance = {
    "Does the state require site developers to maintain stations beyond the minimum 5 years?": [
        ["year", "years"],
        ["maintenance", "maintenance plan"],
    ],
    "How does the state intend to monitor and evaluate site reliability?": [
        ["year", "years"],
        ["maintenance", "maintenance plan"],
    ],
    "What strategies does the state use to ensure continued operation during power outages and extreme weather events?": [
        ["year", "years"],
        ["maintenance", "maintenance plan"],
    ],
    "What types of data does the state plan to collect from the chargers?": [
        ["year", "years"],
        ["maintenance", "maintenance plan"],
    ],
}
