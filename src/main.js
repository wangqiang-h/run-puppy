import { createApp } from 'vue';
import App from './App.vue';
import PhoneFrame from './components/PhoneFrame.vue';
import router from './router'; // 如果你使用了路由

const app = createApp(App);
app.component('PhoneFrame', PhoneFrame);
app.use(router);
app.mount('#app');