import streamlit as st

# App Title
st.title("Custom Armor Customizer")
st.subheader("Create your own custom armor and generate AI-ready descriptions.")

# Sidebar: Armor Customization
st.sidebar.header("Customize Your Armor")

# Under-Armor Options
under_armor = st.sidebar.selectbox(
    "Under Armor (Base Layer)",
    [
        "None",
        "Arming Doublet",
        "Chainmail Hauberk",
        "Leather Jerkin",
        "Brigandine",
        "Padded Gambeson",
        "Silk Undershirt"
    ]
)

# Over-Armor Options
over_armor = st.sidebar.multiselect(
    "Over Armor (Accessories)",
    ["None", "Hooded Cloak", "Flowing Cape", "Heraldic Surcoat", "Fur-Lined Mantle", "Battle Sash", "Royal Tabard"]
)

# Armor Material
armor_material = st.sidebar.selectbox(
    "Armor Material",
    ["Steel", "Bronze", "Gold", "Blackened Iron", "Silver-Plated", "Dragonbone"]
)

# Engraving Style
engraving_style = st.sidebar.selectbox(
    "Engraving Style",
    ["None", "Floral", "Runes", "Geometric", "Battle Scars", "Celestial Engravings"]
)

# Decorative Design Options
design = st.sidebar.selectbox(
    "Decorative Design",
    [
        "None",
        "Floral Engravings",
        "Geometric Patterns",
        "Heraldic Symbols",
        "Mythical Creatures",
        "Royal Crest",
        "Warrior Glyphs"
    ]
)

# Color Customization
st.sidebar.header("Color Customizations")
base_layer_color = st.sidebar.color_picker("Base Layer Color (Tunic/Gambeson)", "#B87333")
armor_accent_color = st.sidebar.color_picker("Armor Accent Color", "#FFD700")
cloak_color = st.sidebar.color_picker("Cloak or Cape Color", "#5B84B1")

# Generate AI Prompt
st.header("Generated AI Prompt")

prompt = f"A warrior clad in {armor_material.lower()} armor. "
if under_armor != "None":
    prompt += f"Underneath, they wear a {under_armor.lower()} dyed {base_layer_color}. "
if over_armor and "None" not in over_armor:
    prompt += f"Over the armor, they wear {', '.join(over_armor).lower()}, dyed {cloak_color}. "
if design != "None":
    prompt += f"The armor is adorned with {design.lower()} designs. "
if engraving_style != "None":
    prompt += f"The engravings feature {engraving_style.lower()} patterns. "
prompt += f"The armor is accented with {armor_accent_color}."

st.text_area("AI Prompt", value=prompt, height=150)

# Next Steps Placeholder
st.header("Next Steps")
st.write("In the next phase, we will integrate AI image generation to visualize your armor.")
