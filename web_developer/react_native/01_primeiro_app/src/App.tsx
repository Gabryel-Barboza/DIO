import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, TouchableOpacity } from 'react-native';

// Crie um arquivo de declaração de tipos global.d.ts para identificar tipos png
import symbolOn from '../assets/pictures/symbol-on.png';
import symbolOff from '../assets/pictures/symbol-off.png';

// Em React Native, tudo é entendido como objeto ou componente
// A função App também é um componente
export default function App() {
  // Sempre retorna uma view de único componente, com outros componentes internos
  // Consulte cada componente pronto na documentação do React Native

  // let isActive = false;

  // [estado, função de mutação de estado]
  const [isActive, setIsActive] = useState(true);

  function handleSymbol() {
    // Permite que a alteração seja renderizada na página
    setIsActive((active: boolean) => {
      // Valor retornado para realizar a mutação
      return !active;
    });
  }

  return (
    <View style={isActive ? styles.containerOn : styles.containerOff}>
      {
        // Comentários em templates JSX são colocados dentro de objetos
        /* Estilos inline 
      os atributos são atribuídos com chaves, pois são tratados como objetos e dentro delas outro objeto para referenciar os estilos inline, chamado objeto de estilização.
      O estilo não é CSS propriamente, porém possui a mesma "cara" para se manter de fácil uso.  */
      }
      <Text style={{ color: 'black', backgroundColor: '#00f08a', fontSize: 30 }}>Olá, mundo!</Text>
      <Text style={styles2.title}>Título</Text>

      <Image
        source={{
          uri: 'https://legacy.reactjs.org/logo-og.png',
        }}
        style={{ width: 100, height: 100 }}
      />

      {/* Adiciona sensividade ao toque
      para que a alteração seja renderizada é preciso alterar o estado. Os componentes são renderizados apenas na primeira vez, quando compilados. A js engine rodando em background interpreta js e permite executar mudanças de estado da app */}
      <TouchableOpacity onPress={handleSymbol}>
        <Image source={isActive ? symbolOn : symbolOff} />
      </TouchableOpacity>

      <StatusBar style="auto" />
    </View>
    // <Text></Text> erro
  );
}

// Estilos internos
const styles2 = StyleSheet.create({
  // Classe do elemento
  title: {
    fontSize: 30,
    color: 'f1f1f1',
  },
});

const styles = StyleSheet.create({
  containerOn: {
    flex: 1,
    backgroundColor: 'black',
    alignItems: 'center',
    justifyContent: 'center',
  },
  containerOff: {
    flex: 1,
    backgroundColor: 'gray',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
