<template>
    <div id='app'>
    <input
    v-model="newTodoText"
    v-on:keyup.enter="addNewTodo"
    placeholder="Add a todo"
  >
  <ul>
    <li
      is="todo-item"
      v-for="(todo, index) in todos"
      v-bind:key="todo.id"
      v-bind:title="todo.title"
      v-bind:asdasd="todo.id"
      v-on:remove="todos.splice(index, 1)"
    ></li>
  </ul>
    </div>
</template>

<script>
window._ = require('lodash');
var Vue = require('Vue');

var tem = {
  template: '\
    <li>\
      {{ title }}\
      {{ asdasd }}\
      <button v-on:click="$emit(\'remove\')">X</button>\
    </li>\
  ',
  props: ['title','asdasd']
}

export default {
  name: 'app',
  data(){
    return{
        newTodoText: '',
        todos: [
          {
            id: 1,
            title: 'Do the dishes',
          },
          {
            id: 2,
            title: 'Take out the trash',
          },
          {
            id: 3,
            title: 'Mow the lawn'
          }
        ],
        nextTodoId: 4
    }
  },
  components: {
    'todo-item' : tem
  },
  methods: {
    addNewTodo: function () {
      this.todos.push({
        id: this.nextTodoId++,
        title: this.newTodoText
      })
      this.newTodoText = ''
    }
  }
  // data () {
  //   return {
  //     msg: 'Welcome to Your Vue.js App'
  //   }
  // }
}
</script>

