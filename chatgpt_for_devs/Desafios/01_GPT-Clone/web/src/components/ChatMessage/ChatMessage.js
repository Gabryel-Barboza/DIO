import React from 'react';
import './ChatMessage.css';
import Avatar from '../../assets/avatar';

// Objeto recebido:
// user (user|chatgpt)
// message - prompt
export const ChatMessage = ({message}) => {
    return (
        <div className={`chat-message ${message.user === 'gpt'} && 'chat-gpt'`}>
            <div className='chat-message-center'>
                <div className={`avatar ${message.user === 'gpt' && 'chat-gpt'}`}>
                    {message.user === 'gpt'&& (<Avatar/>)}
                </div>
                <div className='message'>
                    {message.message}
                </div>
            </div>
        </div>
    )
}
