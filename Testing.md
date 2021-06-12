# Bugs
Issue: The 'Recipes' dropdown menu in the navbar doesn't adapt to the width of the text inside and a vertical scroll bar is displayed.
Furthermore, when clicking on the 'Recipes', the name disappears. 
Solution: according to the documentation of Materialize, you can change the ![constrainWidth](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/contrainwidth.png).
add: { constrainWidth: false } as an option to $(".dropdown-trigger").dropdown() (the dropdown trigger in the javascript file).

Extra: looking at the other options, I added ![coverTrigger](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/covertrigger.png), so the dropdown menu will display below the trigger. And ![hover](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/hover.png), so the dropdown menu will open on hover.
  

