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

ui <- basicPage(h2("Worm-graph"), 
                textInput(inputId = "regex", 
                         label = "Enter a Regular Expression:",
                         value = ""),
                actionButton(inputId = "addButton",
                             label = "Add RegEx"),
                uiOutput("ui"),
                plotOutput("plot"))

app <- shinyApp(ui = ui, server = server)
