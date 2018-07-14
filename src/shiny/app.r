library(shiny)
source("graphbuilder.r")

server <- function(input, output, session) {
  
  output$ui <- renderUI({
    checkboxGroupInput(inputId = "regex.check", label = "Regular Expressions", choices = regexes)
  })

  regexes <- c()

  regex <- reactive({input$regex})

  observeEvent(input$addButton, {
    regex <- regex()
    regexes <<- c(regexes, regex) %>% unique
    updateCheckboxGroupInput(session, "regex.check", choices = regexes)
  })

  observeEvent(input$regex.check, {
    graph <- build.graph(input$regex.check) #FIXME: this fails if the regex is improper 
    print(graph)
  })
  
}

ui <- basicPage(h2("Worm-graph"), 
                textInput(inputId = "regex", 
                         label = "Neuron",
                         value = ""),
                actionButton(inputId = "addButton",
                             label = "Add RegEx"),
                uiOutput("ui"))

app <- shinyApp(ui = ui, server = server)
