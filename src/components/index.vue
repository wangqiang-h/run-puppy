<template>
  <div class="main-container">
    <div class="section">
      <div class="box">
        <div class="wrapper">
          <div class="section-2"><span class="text">9:41</span></div>
        </div>
        <div class="section-3">
          <div class="box-2">
            <div class="section-4"></div>
            <div class="group"></div>
          </div>
        </div>
        <div class="wrapper-2">
          <div class="group-2">
            <div class="img"></div>
            <div class="img-2"></div>
            <div class="img-3"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="pic"></div>
    <span class="text-2">有幸做你生活的小小支点</span>
    <div class="box-3" @click="goToLogin"><span class="text-3">login</span></div>
    <div class="wrapper-3"></div>
    <div class="img-4"></div>
    <span class="text-4">Run<br />Puppy</span>
  </div>
</template>
  
  <script setup>
  import { useRouter } from 'vue-router';

const router = useRouter();

const goToLogin = () => {
  router.push({ name: 'Login' });
};
</script>
  
  <style scoped>
:root {
  --default-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Ubuntu, "Helvetica Neue", Helvetica, Arial, "PingFang SC",
    "Hiragino Sans GB", "Microsoft Yahei UI", "Microsoft Yahei",
    "Source Han Sans CN", sans-serif;
}

.main-container {
  overflow: hidden;
}

.main-container,
.main-container * {
  box-sizing: border-box;
}

input,
select,
textarea,
button {
  outline: 0;
}

.main-container {
  position: relative;
  width: 393px;
  height: 852px;
  margin: 0 auto;
  background: #ffffff;
  overflow: hidden;
}
.section {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 2px;
  position: relative;
  width: 393px;
  margin: 0 0 0 0;
  background: #ffffff;
  backdrop-filter: blur(10px);
}
.box {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 59px;
  z-index: 1;
}
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 0 3px 10px;
  z-index: 2;
}
.section-2 {
  flex-shrink: 0;
  position: relative;
  width: 54px;
  height: 21px;
  z-index: 3;
  border-radius: 24px;
}
.text {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 54px;
  height: 20px;
  top: 1px;
  left: 0;
  color: #000000;
  font-family: SF Pro Text, var(--default-font-family);
  font-size: 16px;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
  white-space: nowrap;
  letter-spacing: -0.32px;
  z-index: 4;
}
.section-3 {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  width: 125px;
  min-height: 0;
  z-index: 5;
}
.box-2 {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 6;
  border-radius: 100px;
}
.section-4 {
  position: absolute;
  width: 80px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(-78.13%, -50%);
  z-index: 7;
  overflow: hidden;
  border-radius: 100px;
}
.group {
  position: absolute;
  width: 37px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(68.92%, -50%);
  z-index: 8;
  overflow: hidden;
  border-radius: 100px;
}
.wrapper-2 {
  display: flex;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 11px 0 0;
  z-index: 9;
}
.group-2 {
  display: flex;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8px;
  position: relative;
  width: 78.401px;
  z-index: 10;
}
.img {
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 12px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103154/signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.img-2 {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103154/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.img-3 {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103154/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.pic {
  position: relative;
  width: 316px;
  height: 221px;
  margin: 211px 0 0 39px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103154/main-image.png)
    no-repeat center;
  background-size: cover;
  z-index: 19;
}
.text-2 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: relative;
  width: 242px;
  height: 24px;
  margin: 37px 0 0 76px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 22px;
  font-weight: 400;
  line-height: 23.98px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 20;
}
.box-3 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  gap: 65px;
  position: relative;
  width: 334px;
  height: 59px;
  margin: 176px 0 0 30px;
  padding: 5px 6px 5px 6px;
  background: #ff5218;
  z-index: 21;
  border-radius: 29.5px;
}
.text-3 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 48px;
  height: 25px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20.448429107666016px;
  font-weight: 500;
  line-height: 24.747px;
  text-align: center;
  white-space: nowrap;
  z-index: 22;
}
.wrapper-3 {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 52px 0 0 130px;
  background: #000000;
  z-index: 15;
  border-radius: 100px;
}
.img-4 {
  position: absolute;
  width: 35px;
  height: 39px;
  top: 116px;
  left: 33px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103154/back-button.svg)
    no-repeat center;
  background-size: cover;
  z-index: 17;
  overflow: hidden;
}
.text-4 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  width: 54px;
  height: 32px;
  top: 119px;
  left: 72px;
  color: #000000;
  font-family: Tsukushi B Round Gothic, var(--default-font-family);
  font-size: 15.862500190734863px;
  font-weight: 400;
  line-height: 15.863px;
  text-align: left;
  text-overflow: initial;
  text-transform: uppercase;
  z-index: 18;
  overflow: hidden;
  -webkit-text-stroke: 0.66px #000000;
}

  
</style>
  