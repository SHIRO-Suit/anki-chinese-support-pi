# Chinese Support PI

Chinese Support PI is a fork of the [Chinese Support 3](https://github.com/Gustaf-C/anki-chinese-support-3) add-on. It works on Anki 24.11.
This fork is a personal extention of features I want to add or things I want to fix.
My primary focus was adding support of a self filling "Stroke Order" field with MDBG gif animation. I used the [Chinese Getter](https://github.com/cadnza/Chinese-Getter) add-on as inspiration.
As well as adding better support for dark mode.

Please refer to the original [Chinese Support 3](https://github.com/Gustaf-C/anki-chinese-support-3) github page for full instructions.
This readme focuses on this fork's features.

## Features

- Automatic field filling
  - Stroke order gifs from [MDBG](https://www.mdbg.net/chinese/dictionary)
- Enhanced dark mode support using [Tomorrow Theme](https://github.com/chriskempson/tomorrow-theme) for Light and Dark styles.

## Usage

To benefit from the stroke order self filling you'll need to add a "Stroke Order" or "笔顺" field in your `Chinese (Advanced)` type.

First make sure you have the `Chinese (Advanced)` type: (if you already have it skip to step 3.)
1. Click `Tools` and `Manage note types`
2. Click `Add` and select `Add: Chinese (Advanced)`
3. Make sure you only have a `Recall` and `Recognition` Type in your `chinese (Advanced)` type. (In the dropdown in Add>Cards>Card>Card Type.) Coming from the original `Chinese support 3` Addon, I had type conflicts with the PI version where it would generate a lot of cards mostly with the wrong template (html+css). I solved it by deleting the types, and reinstalling the `chinese (Advanced)` type.
 

To add the field:

1. Add a new note to Anki (press *a*)
2. In `Type` select `Chinese (Advanced)` as the note type
3. Click `Fields`
4. In the popup click `Add` then type `Stroke Order` or `笔顺` and click OK. (See `config.json` for a list of valid field names.)
5. Click Save.
6. The animations should now auto-fill the `Stroke Order` field like the other fields when you press Tab.

<br>



## Screenshots

![Screenshot #1](https://raw.githubusercontent.com/Gustaf-C/anki-chinese-support/master/screenshots/add-card.png)

![Screenshot #2](https://raw.githubusercontent.com/Gustaf-C/anki-chinese-support/master/screenshots/view-card.png)

<br>
