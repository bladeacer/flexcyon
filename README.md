<p align="left">
    <a href="https://www.moritzjung.dev/obsidian-stats/themes/flexcyon-1/">
        <img src="https://img.shields.io/badge/dynamic/json?query=%24%5B%22flexcyon%22%5D.download&url=https%3A%2F%2Freleases.obsidian.md%2Fstats%2Ftheme&style=for-the-badge&label=Downloads&logo=obsidian" referrerpolicy="noreferrer">
    </a>
    <a href="https://github.com/bladeacer/flexcyon/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/bladeacer/flexcyon?style=for-the-badge" referrerpolicy="noreferrer"> 
    </a>
    <a href="https://github.com/bladeacer/flexcyon/releases/latest">
        <img src="https://img.shields.io/github/v/release/bladeacer/flexcyon?style=for-the-badge&sort=semver" referrerpolicy="noreferrer">
    </a>
</p>

> The documentation is in the process of a refactor. Links may be broken.
> I will update this page once I have the new documentation ready.

## About Flexcyon

A Obsidian theme combining the colour schemes of Halcyon and Flexoki.

I really liked the vibrant colours of the [Halcyon colour scheme](https://halcyon-theme.netlify.app/), and the inky aesthetic of the [Flexoki colour scheme](https://stephango.com/flexoki). Hence, I decided to combine the two which started this theme.

There is also a light mode colour scheme combining [Origami theme's](https://github.com/7368697661/Origami) and Flexoki light's colour schemes.

## Screenshots

![Figure 1: ASCII Art, Dimmed File Extensions](./docs/showcase1.png)

![Figure 2: Vim Status Mode, Coloured Headings, Hide Until Hover Status Bar](./docs/showcase2.png)

![Figure 3: Dimmed Inactive Settings navigation, smiley and coloured icons](./docs/showcase3.png)

![Figure 4: Light Mode with Powerlevel10k layout and status style](./docs/showcase4.png)

## Installation via community store (recommended)

To install this theme via the community store, navigate to `Settings > Appearance`

1. Under `Themes`, click Manage
2. `Type "Flexcyon in the search bar > Select it > Click "Install and Use"`

Installation of [Style Settings](#style-settings) is highly recommended for this theme, as most customisation and functionality is built around it.

### Installation via BRAT

To install this theme via BRAT, navigate to `Settings > Community Plugins > Browse`

1. `Type "BRAT" in the search bar > Select it (the one by TftHacker) > Click install`
2. Wait for installation to complete then click `Enable`
3. Click `Options`
4. Click `Add Beta Theme`
5. Input `https://github.com/bladeacer/flexcyon` and then click `Add Theme`

## Documentation

A huge thanks to GitHub Pages for hosting the documentation at https://flexcyon.github.io/docs-en/

> I want to keep the docs and source code separate, the documentation is currently being reworked.
> The old documentation is now fully deprecated and its links will not work.
> (was https://flexcyon-docs.readthedocs.io/en/latest )

## Features

[Here is a web showcase](https://share.note.sx/j4wqojpy#xi8TbTY58w4JaoiHcPdRJA+V60W3jT0qDoLyUhkTE3U) of the features this theme has to offer.

- Some features will not have a 1 to 1 correspondence to the main theme, but this site should give you a preview of how the theme looks before installing it

#### What this theme has

- vim mode status (when using builtin vim keybinds)
- Status bar options like Powerlevel10k inspired status bar styling
- Smiley toggle icons and other options for settings
- ASCII art or custom quote in new empty tabs
- subtle opacity effects for UI elements
- a light and dark mode colour scheme
- ASCII checkboxes
- Heading options like underline, numbered, coloured
- A plethora of cssclasses and callout customisation options
<!-- - A [plethora of cssclasses and callout customisation options](https://flexcyon-docs.readthedocs.io/en/latest/Styling/CSS-Classes/) -->
- Workspace Layouts like card layout with TUI inspired add-on, angled layout
- Configure left, right sidebar and modal background images
- Animation options for tabs
- And many more...

![Figure 5: ASCII checkboxes](./docs/ascii_checkboxes1.png)

#### What this theme does not have

- multiple colour schemes (though you can override the existing one with your own, see [Style Settings](#style-settings))
- alternate checkboxes
- embedded fonts, svgs

#### Supported plugins/snippets

The following plugins/snippets are officially supported:

##### Plugins

- [File Tree Alternative by Ozan Tellioglu](https://github.com/ozntel/file-tree-alternative)
- [Highlightr by Chetachi](https://github.com/chetachiezikeuzor/Highlightr-Plugin)
- [Minitabs by ssjy1919](https://github.com/ssjy1919/Obsidian-minitabs)
- [Full Calendar by Davis Haupt](https://github.com/obsidian-community/obsidian-full-calendar)
- [Breadcrumbs by SkepticMystic](https://github.com/SkepticMystic/breadcrumbs)
- [Spaced Repetition by Stephen Mwangi](https://github.com/st3v3nmw/obsidian-spaced-repetition)
- [Dataview by Michael Brenan](https://github.com/blacksmithgu/obsidian-dataview)
- [Vault Statistics by Bryuan Kyle](https://github.com/bkyle/obsidian-vault-statistics-plugin)
- [Calendar by Liam Cain](https://github.com/liamcain/obsidian-calendar-plugin)
- [Kanban by mgmyers](https://github.com/mgmeyers/obsidian-kanban)
- [Omnisearch by scambier](https://github.com/scambier/obsidian-omnisearch)

##### Snippets

- [CSS Banners snippet by HandaArchitect](https://github.com/HandaArchitect/obsidian-banner-snippet)

For plugins/snippets that are not styled yet, feel free to open a Pull Request/Feature Request/start a Discussion on it.

#### Roadmap

<!-- The Roadmap for this theme can be found [here](https://flexcyon-docs.readthedocs.io/en/latest/README/roadmap/). -->

The Roadmap for this theme is currently in the works, stay tuned.

#### Changelogs

<!-- The Changelogs for this theme can be found [here](https://flexcyon-docs.readthedocs.io/en/latest/changelogs/) -->

The Changelogs for this theme is currently in the works, stay tuned.

#### Questions, Issues?

Feel free to talk about it at:

- [this Discord thread](https://discord.com/channels/686053708261228577/1338130333698359357).
- [this Obsidian forum topic](https://forum.obsidian.md/t/flexcyon-a-dark-theme-for-obsidian/99869)

Alternatively, you can open an issue at [the repository](https://github.com/bladeacer/flexcyon/issues) or [start a GitHub discussion](https://github.com/bladeacer/flexcyon/discussions) here.

## Design Principles

This theme tries to:

- be "reasonably opinionated"
  - opt into customisation instead opting out of customisation
- be decently lightweight, meaning:
  - fonts, svgs and the like are not embedded in this theme
  - (hopefully) sane defaults, customisable with style settings
- dim inactive or unfocused UI elements to reduce information overload
- have a decent feature set of style settings for customisation
- bundle numerous callout metadata utilites

## Style Settings

<!-- Documentation for style settings of this theme can be found [here](https://flexcyon-docs.readthedocs.io/en/latest/Styling/Style-Settings) -->

Documentation for style settings of this theme is in the works, stay tuned.

Documentation on installing and using style settings can be found [here](https://github.com/mgmeyers/obsidian-style-settings)

## License

This theme is licensed under the [MIT License](https://github.com/bladeacer/flexcyon/blob/master/LICENSE)

## Credits

<!-- See https://flexcyon-docs.readthedocs.io/en/latest/credits/ -->

Credits for this theme is in the works, stay tuned.
