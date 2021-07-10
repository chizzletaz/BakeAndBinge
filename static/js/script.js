$(document).ready(function () {
    $(".dropdown-trigger").dropdown({ 
        constrainWidth: false,
        coverTrigger: false,
        });
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('textarea#recipe_description').characterCounter();
    $('.tabs').tabs();
    // $('.modal').modal();
    $('.modal').modal({
        ready: function() {
        $('.carousel.carousel-slider').carousel({fullWidth: true});
        }
      });
      $('#demo-carousel-indicators').carousel({fullWidth: true});
      $('.carousel.carousel-slider').carousel({fullWidth: true});

    // Credit: Flask mini project: Materialize for validation
    // https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/04-AddingATask-WritingToTheDatabase/02-materialize-select-validation/templates/add_task.html

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
    /* end credit */
});

$("#copyright").text(new Date().getFullYear()); 

// Credit: https://shouts.dev/add-or-remove-input-fields-dynamically-using-jquery
// add_recipe.html
// add ingredient row
$("#addRowIngredient").click(function () {
    var html = `
    <div class="row mb0">
        <div class="input-field col s12 mb0">
            <textarea id="ingredient[]" name="ingredient[]" class="materialize-textarea" required></textarea>
            <label for="ingredient">Ingredient</label>
            <i id="removeRowIngredient" class="far fa-trash-alt prefix right"></i>    
        </div>`;

    $('#newRowIngredient').append(html);
});
// remove ingredient row
$(document).on('click', '#removeRowIngredient', function () {
    $(this).parent('div').remove();
});

// add instruction row
$("#addRowStep").click(function () {
    var html = `
    <div class="row mb0">
        <div class="input-field col s12 mb0">
            <textarea id="step" name="step[]" class="materialize-textarea" required></textarea>
            <label for="step">Instruction</label>
            <i id="removeRowStep" class="far fa-trash-alt prefix right"></i>    
        </div>`;

    $('#newRowStep').append(html);
});

// remove instruction row
$(document).on('click', '#removeRowStep', function () {
    $(this).parent('div').remove();
});