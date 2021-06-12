$(document).ready(function () {
    $(".dropdown-trigger").dropdown({ 
        hover: true, 
        constrainWidth: false,
        coverTrigger: false,
        });
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
});

// add_recipe.html
// add ingredient row
$("#addRowIngredient").click(function () {
    var html = `
    <div class="row mb0" id="inputIngredientRow">
        <div class="input-field col s12 mb0">
            <input id="ingredient" name="ingredient[]" type="text" class="validate">
            <label for="ingredient">Ingredient</label>
            <i id="removeRowIngredient" class="far fa-trash-alt prefix right"></i>    
        </div>`;

    $('#newRowIngredient').append(html);
});


// remove ingredient row
$(document).on('click', '#removeRowIngredient', function () {
    $(this).closest('#inputIngredientRow').remove();
});

// add instruction row
$("#addRowStep").click(function () {
    var html = `
    <div class="row mb0" id="inputStepRow">
        <div class="input-field col s12 mb0">
            <input id="step" name="step[]" type="text" class="validate">
            <label for="step">Instruction</label>
            <i id="removeRowStep" class="far fa-trash-alt prefix right"></i>    
        </div>`;

    $('#newRowStep').append(html);
});

// remove instruction row
$(document).on('click', '#removeRowStep', function () {
    $(this).closest('#inputStepRow').remove();
});