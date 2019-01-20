library(shiny)
source("graphbuilder.r")

server <- function(input, output, session) {
  
  output$ui <- renderUI({
    checkboxGroupInput(inputId = "regex.check", label = "", choices = regexes) # creates the checkbox
  })

  regexes <- c() # initial collection of regexes

  regex <- reactive({input$regex}) # grabs the regex from the text box

  observeEvent(input$addButton, {
    regex <- regex()
    regexes <<- c(regexes, regex) %>% unique
    updateCheckboxGroupInput(session, "regex.check", choices = regexes) # updates the checkbox with the new regex
  })

  observeEvent(input$regex.check, {
    graph <- build.graph(input$regex.check) #FIXME: this fails if the regex is improper 
    output$plot <-renderPlot({show.graph(graph)}) # creates the plot with the selected regexes
  })
  
}

ui <- basicPage(h2("Exploring the C. elegans Connectome"), 
                p("The nematode C. elegans' neuron graph has been mapped completely, giving a total picture of the conections in its brain. To explore these connections, enter a regular expression in the text box below. When a regular expression is selected, worm-graph generates a graph of all the neruons that match the expression. Expressions can be nested, to give a more complete image of the brain topography."),
                textInput(inputId = "regex", 
                         label = "Enter a Regular Expression:",
                         value = ""),
                actionButton(inputId = "addButton",
                             label = "Add RegEx"),
                uiOutput("ui"),
                plotOutput("plot"))

app <- shinyApp(ui = ui, server = server)
