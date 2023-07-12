from PIL import Image, ImageDraw, ImageFont


def generate_card(image_path: str, name: str, species: str):
    card_width, card_height = 1200, 630

    card_image = Image.new('RGB', (card_width, card_height), 'white')
    render_img = ImageDraw.Draw(card_image)

    def avatar(img_path: str, coords: list[int, int]):
        x, y = coords

        avatar_img = Image.open(img_path)

        size = min(avatar_img.size) // 3
        avatar_img = avatar_img.resize((size, size))

        mask = Image.new('L', avatar_img.size, 0)
        draw_img_mask = ImageDraw.Draw(mask)
        draw_img_mask.rounded_rectangle(((0, 0), (size, size)), fill=255, radius=16 * 2)
        card_image.paste(avatar_img, (x, y), mask=mask)

    def text_field(coords: list[int, int], heading: str, value: str):
        x, y = coords
        font = ImageFont.truetype('fonts/OpenSans-VariableFont_wdth,wght.ttf', 48)

        name_position = (x, y)
        occupation_position = (x, y + 50)

        render_img.text(name_position, f'{heading}', fill='black', font=font)
        render_img.text(occupation_position, f'{value}', fill='black', font=font)

    avatar(image_path, [(card_height // 7), 150])
    text_field([50, 100], 'Name', name)
    text_field([250, 100], 'Species', species)

    card_image.save('generated_card_image.png')

    print('Card image generated successfully!')


if __name__ == "__main__":
    generate_card('test.png', 'Kuro', 'Fusky')
