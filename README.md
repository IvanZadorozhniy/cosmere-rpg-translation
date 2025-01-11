# Aim of the repository
I use this repository for storing files that I translated for my game party in Foundry VTT for cosmere rpg system. You can find the system [here](https://github.com/the-metalworks/cosmere-rpg)

Also I translated the playtest material from the same team. It can be found [here](https://github.com/the-metalworks/cosmere-rpg-worlds)

# What exactly does it do?
There is a great module that uses Babele to translate other modules in Russian, it is the [Phantom module](https://github.com/phenomen/foundry-vtt-ru). I use it as a base for translation. It change files in runtime for users who set Russian as main language. Below, you can see the difference in one image:
![Example of Translation](https://github.com/IvanZadorozhniy/images_repo/blob/main/cosmere-rpg-translation/Screenshot_2025-01-11_14-13-26.jpg)

# So how to use it?
1. Install cosmere-rpg [system](https://github.com/the-metalworks/cosmere-rpg) and [playtest](https://github.com/the-metalworks/cosmere-rpg-worlds) material from metalwork 
2. Install [Phantom module](https://github.com/phenomen/foundry-vtt-ru) for translation 
3. Go to the modules folder in your FoundryVTT folder (you can find it in settings on the main screen of Foundry)
![Path to UserData in Foundry](https://github.com/IvanZadorozhniy/images_repo/blob/main/cosmere-rpg-translation/Screenshot_2025-01-11_14-24-33.jpg)
4. Find ru-ru module and go there
5. You should find there couple folders:
![ru-ru module](https://github.com/IvanZadorozhniy/images_repo/blob/main/cosmere-rpg-translation/Screenshot_2025-01-11_14-26-43.jpg)
6. Move files from this repo to the same folders in the ru-ru module
7. In the module.json, you have to add code belove into the languages object
```
{
    "lang": "ru",
    "name": "cosmere-rpg",
    "path": "i18n/systems/cosmere-rpg.json"
}
```
8. Fully restart the FoundryVTT
9. Set the Russian language in the setting and reload 
10. Here we are, it should work. 

There is a "copy_files.py" file. I **highly don't recommend** to use it, but if you know what you do you can use it 
``` python copy_files.py -p "Your Foundry User Data Path" ```
