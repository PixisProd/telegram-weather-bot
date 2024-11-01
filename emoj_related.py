def get_emoji_for_description(description):
            match description["weather"][0]["main"]:
                case "Rain": return '🌧️'
                case "Thunderstorm": return '⛈️'
                case "Drizzle": return '🌦️'
                case "Snow": return '🌨️'
                case "Atmosphere": return '🌫️'
                case "Clear": return '☀️'
                case "Clouds": return '☁️'
                case _ : return ' '
        
def get_country_flag(country_code):
    data = country_code["sys"]["country"]
    return (
    chr(0x1F1E6 + ord(data[0]) - ord('A')) +
    chr(0x1F1E6 + ord(data[1]) - ord('A'))
    )

def get_emohi_for_feels_like(description):
    data = description["main"]["feels_like"]
    if data < 0: return '❄️'
    elif data < 20: return '🌥️'
    else: return '☀️'