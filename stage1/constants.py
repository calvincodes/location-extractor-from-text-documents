# TODO: Update labels as you add more features
labels = ['Word', 'F1', 'F2', 'F3', 'Class']

neighboring_verbs_for_negative_examples = ['has', 'have', 'had', 'was', 'were', 'with', 'would', 'sea',
                                           'of', 'times', 'post', 'against', 'should', 'will', 'wont',
                                           'not', 'do', 'does']


neighboring_words = ['over', 'around', 'to', 'from', 'at', 'in', 'between', 'the',
                     'of', 'where', 'with', 'when', 'and', 'outside']

# TODO: UPDATE THIS LIST OF BLACKLISTED RULE WORDS
blacklisted_rule_words = \
    ['Mr.', 'May', 'American', 'Indian',
        'a', 'an', 'the', 'have', 'has', 'been', 'was', 'is', 'by', 'to', 'at', 'for', 'in', 'of', 'from', 'like', 'with',
     'were', 'are', 'what', 'where', 'how', 'why', 'who', 'it', "it's", 'and', 'but', 'on', "its", 'we', 'our', 'over',
     'under', "about", "upon", "these", "those", "this", "that", "i", "they", "them"]

# TODO: UPDATE WHITELISTED WORDS FOR ANY POTENTIAL OUTLIERS
# whitelisted_words = []
whitelisted_words = ['Momofuku Nishi', 'Berlin', 'Hong Kong', 'Asia', 'Paraba', 'Afghanistan', 'JERUSALEM', 'So Paulo',
                     'San Diego', 'TEHRAN', 'Capitol Hill', 'East Jerusalem', 'Libya', 'Zhejiang', 'Kuwait',
                     'Westchester', 'Manhattan', 'Shandong', 'Maale Adumim', 'Vancouver Island', 'Qum',
                     'India', 'Manchester', 'Fort Lauderdale', 'Bamberton', 'Roraima', 'Tokyo', 'Bellevue', 'Seattle',
                     'Havana', 'RIO DE JANEIRO', 'Sweden', 'LONDON', 'San Francisco', 'Columbus', 'Banff', 'Brazil',
                     'Dakar', 'California', 'Hollywood', 'ISTANBUL', 'South Carolina', 'Boa Vista', 'Kenya',
                     'Guantnamo Bay', 'JIUQUAN', 'Syria', 'Linyi', 'LOS ANGELES', 'Alaska', 'Toronto', 'HAVANA',
                     'Lashkar Gah', 'central New York', 'Haifa', 'Las Vegas', 'Lesbos', 'Long Island',
                     'Azerbaijan', 'England', 'Helmand', 'SAN','FRANCISCO','SAN FRANCISCO', 'Disney World', 'Netherlands',
                     'Buchanan', 'Ankara', 'Bronx', 'U S', 'Australia', 'Baltimore', 'Gansu', 'Norwalk', 'Jiuquan',
                     'Saudi Arabia', 'Sierra Nevada', 'Arizona', 'Brussels', 'Washington', 'Hawthorne', 'PARIS',
                     'White Plains', 'Gothenburg', 'Istanbul', 'Louisiana', 'HONG KONG', 'Greece', 'Izmir', 'Nashville',
                     'Fundao Getlio Vargas', 'Chicago', 'Taiwan', 'Bahrain', 'Arkansas', 'Rockville', 'N J', 'S C',
                     'Charleston', 'America', 'Alabama', 'Hawaii', 'Orlando', 'Greenwich Village', 'Louisville',
                     'State of Palestine', 'France', 'Silicon Valley', 'United Arab Emirates', 'MONTICELLO',
                     'WASHINGTON', 'China', 'Westbury', 'Kunduz', 'Canada', 'Natal', 'Monmouth', 'Colorado',
                     'White House', 'Dallas', 'FORT LAUDERDALE', 'Katowice', 'Kansas City', 'Matamoros', 'Gainesville',
                     'New York City', 'Indonesia', 'Paris', 'CHICAGO', 'Central America', 'London',
                     'Eastern United States','United','States', 'Sandringham', 'Sochi', 'Tennessee', 'Davos', 'Jerusalem',
                     'Switzerland', 'Strait of Hormuz', 'Yemen', 'White House', 'North Africa', 'New York',
                     'Brooklyn', 'northeastern Brazil', 'Miami', 'BEVERLY HILLS', 'New Delhi', 'Philadelphia',
                     'United States', 'KABUL', 'Britain', 'Chengdu', 'Jalisco', 'Massachusetts', 'Europe', 'DUBLIN',
                     'KANSAS', 'Georgia', 'MEXICO CITY', 'Monticello', 'Tampa', 'Maryland', 'Africa', 'Iran',
                     'Amazonas', 'Wilmington', 'Calif', 'Minnesota', 'SoHo', 'Albany', 'Malvern', 'Atlanta',
                     'United States of America', 'Montana', 'Cleveland', 'Los Angeles', 'ESCONDIDO', 'Germantown',
                     'South Korea', 'Ardsley', 'Moria', 'San Antonio', 'Lexington Avenue', 'CHENGDU', 'Escondido',
                     'Ukraine', 'PITTSBURGH', 'Myanmar', 'MEXICO', 'southwest China', 'Florida', 'Ireland', 'SEATTLE',
                     'Cuba', 'Pittsburgh', 'Omaha', 'Manaus', 'Iraq', 'El Salvador', 'Topeka', 'Rio Grande do Norte',
                     'Broward County', 'Eastern Europe the Balkans', 'Anchorage', 'Kandahar', 'TOPEKA', 'Texas',
                     'Moscow', 'Davos', 'Annapolis', 'Mexico', 'North Dakota', 'Clinton Hill', 'San Jose', 'Cancn',
                     'DETROIT', 'Indiana', 'Sacramento', 'Iowa', 'READING', 'Japan', 'Michigan', 'Queens', 'Guatemala',
                     'Detroit', 'Russia', 'English Channel', 'northern Tehran', 'Kabul', 'Benghazi', 'West Jerusalem',
                     'BEIJING', 'Germany', 'Portland', 'AMERICA', 'Guadalajara', 'Midtown Manhattan', 'Israel',
                     'Poland', 'Turkey', 'COVINGTON', 'VANDENBERG AIR FORCE BASE', 'Somalia', 'Oval Office', 'ATLANTA',
                     'Takata', 'Connecticut', 'Kentucky', 'La Jolla', 'Kansas', 'Beijing', 'New Jersey', 'Idaho',
                     'ROSWELL', 'Richmond', 'Vietnam', 'Boston', 'SEOUL', 'Senegal', 'Oxford', 'N Y', 'Tehran',
                     'HOUSTON', 'Southern California', 'Chad', 'Carol City']
